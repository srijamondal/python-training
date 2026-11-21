from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Review
from .forms import Registrationform, ReviewForm


# ---------- Step 6 & 10: Home page with search ----------
def home(request):
    query = request.GET.get('q', '')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies, 'query': query})


# ---------- Step 7 & 9: Movie details + add review ----------
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()

    # Check if the logged-in user has already reviewed this movie
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(movie=movie, user=request.user).first()

    form = ReviewForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        if user_review:
            messages.warning(request, 'You have already reviewed this movie.')
            return redirect('movie_detail', movie_id=movie.id)

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            messages.success(request, 'Your review has been added.')
            return redirect('movie_detail', movie_id=movie.id)

    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
        'user_review': user_review,
    }
    return render(request, 'movies/movies_details.html', context)


# ---------- Step 8: Registration ----------
def register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('home')
    else:
        form = Registrationform()
    return render(request, 'registration/register.html', {'form': form})


# ---------- Step 11: Edit review ----------
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated.')
            return redirect('movie_detail', movie_id=review.movie.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'movies/edit_review.html', {'form': form, 'review': review})


# ---------- Step 11: Delete review ----------
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    movie_id = review.movie.id

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        return redirect('movie_detail', movie_id=movie_id)

    return render(request, 'movies/delete_review.html', {'review': review})