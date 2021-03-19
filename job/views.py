from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from job.models import Applicant, Recruiter, Job


# Create your views here.
def index(request):
    context = {}
    return render(request, 'job/common/index.html', context)


def Logout(request):
    logout(request)
    return redirect('index')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'job/admin/admin_home.html')


def view_applicants(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    applicants = Applicant.objects.all()
    context = {
        'applicants': applicants,
    }
    return render(request, 'job/admin/view_applicants.html', context)


def view_recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiters = Recruiter.objects.all()
    context = {
        'recruiters': recruiters,
    }
    return render(request, 'job/admin/view_recruiters.html', context)


def delete_applicant(request, pk):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    applicant = User.objects.get(id=pk)
    applicant.delete()
    return redirect('view_applicants')


def delete_recruiter(request, pk):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = User.objects.get(id=pk)
    recruiter.delete()
    return redirect('view_recruiters')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiters = Recruiter.objects.filter(status='pending')
    context = {
        'recruiters': recruiters,
    }
    return render(request, 'job/admin/recruiter_pending.html', context)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiters = Recruiter.objects.filter(status='approved')
    context = {
        'recruiters': recruiters,
    }
    return render(request, 'job/admin/recruiter_accepted.html', context)


def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiters = Recruiter.objects.filter(status='rejected')
    context = {
        'recruiters': recruiters,
    }
    return render(request, 'job/admin/recruiter_rejected.html', context)


def change_status(request, pk):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    recruiter = Recruiter.objects.get(id=pk)
    if request.method == 'POST':
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
    context = {
        'recruiter': recruiter,
        'error': error,
    }
    return render(request, 'job/admin/change_status.html', context)


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/admin/admin_login.html', context)


def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpwd']
        n = request.POST['newpwd']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/admin/change_password.html', context)


def applicant_home(request):
    if not request.user.is_authenticated:
        return redirect('applicant_login')
    context = {}
    return render(request, 'job/applicant/applicant_home.html', context)


def applicant_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                applicant = Applicant.objects.get(user=user)
                if applicant.type == "student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/applicant/applicant_login.html', context)


def applicant_signup(request):
    error = ""
    if request.method == 'POST':
        l = request.POST['lname']
        f = request.POST['fname']
        e = request.POST['email']
        m = request.POST['mobile']
        p = request.POST['pwd']
        g = request.POST['gender']
        i = request.FILES['image']
        try:
            user = User.objects.create_user(last_name=l, first_name=f, username=e, password=p)
            Applicant.objects.create(user=user, mobile=m, image=i, gender=g, type="student")
            error = "no"
        except:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/applicant/applicant_signup.html', context)


def applicant_change_password(request):
    if not request.user.is_authenticated:
        return redirect('applicant_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpwd']
        n = request.POST['newpwd']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/applicant/change_password.html', context)


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        l = request.POST['lname']
        f = request.POST['fname']
        e = request.POST['email']
        m = request.POST['mobile']
        g = request.POST['gender']
        c = request.POST['company']

        recruiter.user.last_name = l
        recruiter.user.first_name = f
        recruiter.mobile = m
        recruiter.gender = g
        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error = "no"
        except:
            pass
    context = {
        'recruiter': recruiter,
        'error': error,
    }
    return render(request, 'job/recruiter/recruiter_home.html', context)


def recruiter_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                recruiter = Recruiter.objects.get(user=user)
                if recruiter.type == "recruiter" and recruiter.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/recruiter/recruiter_login.html', context)


def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        l = request.POST['lname']
        f = request.POST['fname']
        e = request.POST['email']
        m = request.POST['mobile']
        p = request.POST['pwd']
        g = request.POST['gender']
        c = request.POST['company']
        i = request.FILES['image']
        try:
            user = User.objects.create_user(last_name=l, first_name=f, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=m, image=i, gender=g, company=c, type="recruiter",
                                     status="pending")
            error = "no"
        except:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/recruiter/recruiter_signup.html', context)


def recruiter_change_password(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpwd']
        n = request.POST['newpwd']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/recruiter/change_password.html', context)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        title = request.POST['title']
        start_date = request.POST['startdate']
        end_date = request.POST['enddate']
        salary = request.POST['salary']
        logo = request.FILES['logo']
        experience = request.POST['exp']
        location = request.POST['location']
        skills = request.POST['skills']
        desc = request.POST['desc']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, title=title, start_date=start_date, end_date=end_date,
                               salary=salary, image=logo, created=date.today(), location=location,
                               experience=experience, skills=skills, description=desc, )
            error = "no"
        except:
            error = "yes"
    context = {
        'error': error,
    }
    return render(request, 'job/recruiter/add_job.html', context)


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    jobs = Job.objects.filter(recruiter=recruiter)
    context = {
        'jobs': jobs,
    }
    return render(request, 'job/recruiter/job_list.html', context)


def edit_job(request, pk):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST['title']
        start_date = request.POST['startdate']
        end_date = request.POST['enddate']
        salary = request.POST['salary']
        experience = request.POST['exp']
        location = request.POST['location']
        skills = request.POST['skills']
        desc = request.POST['desc']

        job.title = title
        job.salary = salary
        job.experience = experience
        job.location = location
        job.skills = skills
        job.description = desc
        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        if start_date:
            try:
                job.start_date = start_date
                job.save()
            except:
                pass
        else:
            pass
        if end_date:
            try:
                job.end_date = end_date
                job.save()
            except:
                pass
        else:
            pass
    context = {
        'error': error,
        'job': job,
    }
    return render(request, 'job/recruiter/job_edit.html', context)


def delete_job(request, pk):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect('view_recruiters')


def change_company_logo(request, pk):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        logo = request.FILES['logo']
        job.image = logo
        try:
            job.save()
            error = "no"
        except:
            error = "yes"
    context = {
        'error': error,
        'job': job,
    }
    return render(request, 'job/recruiter/change_company_logo.html', context)
