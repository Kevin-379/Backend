from .models import ProfessorReview, Professor, CourseReview


def prof_reviews(request):
    results = []
    if request.GET:
        print('here')
        profs = Professor.objects.all()
        query = request.GET.get('search')
        if query:
            print(query)
            query_list = query.split()
            for q in query_list:
                print(q)
                for prof in profs:
                    print(prof.name)
                    if q.lower() in prof.name:
                        results.append(profs.filter(name=prof.name).first())
    if len(results) > 5:
        results = results[:5]
    return {'prof_review': ProfessorReview.objects.order_by('-time')[:5],
            'course_review': CourseReview.objects.order_by('-time')[:5],
            'results': results}
