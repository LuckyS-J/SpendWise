from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView, Response
from .serializers import CategorySerializer, TransactionSerializer
from .models import Category, Transaction
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

# Create your views here.


def Home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                user = authenticate(
                    request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('Home-page')
            except User.DoesNotExist:
                form.add_error('email', 'Incorrect email or password.')
    else:
        form = LoginForm()
    return render(request, 'SpendApp/index.html', {'form': form})


def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request, 'SpendApp/register.html', {'form': form})


@login_required
def HomePage(request):
    return render(request, 'SpendApp/home-page.html')


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TransactionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(
            user=request.user).order_by('-date')
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TransactionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Transaction.objects.get(pk=pk, user=user)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response({'error': 'Not found'}, status=404)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response({'error': 'Not found'}, status=404)
        serializer = TransactionSerializer(
            transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response({'error': 'Not found'}, status=404)
        transaction.delete()
        return Response(status=204)


class TransactionSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        total_spent = transactions.aggregate(Sum('amount'))['amount__sum'] or 0

        by_category = transactions.values('category__name').annotate(
            total=Sum('amount')
        ).order_by('-total')

        return Response({
            'total_spent': total_spent,
            'by_category': by_category
        })
