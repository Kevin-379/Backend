from django.shortcuts import render, get_object_or_404
from .models import ProfessorReview, Professor, CourseReview, Course
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    return render(request, 'portal/home.html')


def about(request):
    return render(request, 'portal/about.html')


class ProfReviewListView(ListView):
    model = ProfessorReview
    template_name = 'portal/home.html'
    context_object_name = 'prof_review'
    ordering = ['-time']
    paginate_by = 5


class ProfReviewDetailView(DetailView):
    model = ProfessorReview


class ProfReviewCreateView(LoginRequiredMixin, CreateView):
    model = ProfessorReview
    fields = ['name', 'courses_taught', 'rating', 'difficulty', 'comments']

    def update(self, form):
        name = form.cleaned_data.get('name').lower()
        courses_taught = form.cleaned_data.get('courses_taught').lower()
        rating = form.cleaned_data.get('rating')
        if rating > 5:
            rating = 5
        if rating < 0:
            rating = 0

        prof = Professor.objects.filter(name=name).first()

        if prof == None:
            Professor.create(name, courses_taught, rating)
        else:
            updated_courses = prof.courses_taught

            for course in courses_taught:
                if course not in updated_courses:
                    updated_courses = updated_courses.append(course)

            prof.save(courses_taught=updated_courses)
            updated_rating = (prof.rating*prof.total+rating)/(prof.total+1)
            updated_total = prof.total + 1
            prof.save(rating=updated_rating, total=updated_total)

    def form_valid(self, form):
        self.update(form)
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProfReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProfessorReview
    fields = ['rating', 'difficulty', 'comments']

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.get_object().changed = True
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author


class ProfReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProfessorReview
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author


class UserProfReviewListView(ListView):
    model = CourseReview
    template_name = 'portal/user_reviews.html'
    context_object_name = 'reviews'
    ordering = ['-time']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return CourseReview.objects.filter(author=user).order_by('-time')


class CourseReviewListView(ListView):
    model = CourseReview
    template_name = 'portal/home.html'
    context_object_name = 'prof-review'
    ordering = ['-time']
    paginate_by = 5


class CourseReviewDetailView(DetailView):
    model = CourseReview


class CourseReviewCreateView(LoginRequiredMixin, CreateView):
    model = CourseReview
    fields = ['code', 'taught_by', 'rating', 'difficulty', 'requirements', 'recommended_for', 'comments']

    def update(self, form):
        code = form.cleaned_data.get('code')
        rating = form.cleaned_data.get('rating')
        if rating > 5:
            rating = 5
        if rating < 0:
            rating = 0

        course = Course.objects.filter(code=code).first()

        if course == None:
            Course.create(code, rating)
        else:
            updated_rating = (course.rating*course.total+rating)/(course.total+1)
            updated_total = course.total + 1
            course.update(rating=updated_rating, total=updated_total)

    def form_valid(self, form):
        self.update(form)
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CourseReview
    fields = ['rating', 'difficulty', 'taught_by', 'requirements', 'recommended_for', 'comments']

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.get_object().changed = True
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author


class CourseReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CourseReview
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author


'''
class UserProfReviewListView(ListView):
    model = ProfessorReview
    template_name = 'portal/user_reviews.html'
    context_object_name = 'reviews'
    ordering = ['-time']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ProfessorReview.objects.filter(author=user).order_by('-time')
'''