from django.shortcuts import render , redirect
from.models import comment , message , posts
from.forms import CommentForm
# Create your views here.
def first (request):
        # إنشاء session إذا لم يكن موجود
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    if request.method =='POST':
        N=request.POST.get('name')
        C=request.POST.get('comment')
        if not comment.objects.filter(session_id=session_id).exists():
            data = comment( name = N , comment = C , session_id=session_id)
            data.save()
            return redirect('home') # type: ignore
        else:
            # إذا حاول الزائر إضافة تعليق ثاني
            return render(request, 'work.html', {
                'CT': comment.objects.all(),
                'error': "you alreday whriting comment"
            })
    return render(request , 'work.html'  , {'CT':comment.objects.all()} )
def contact (request):
    if request.method == 'POST':
        un=request.POST.get('username')
        E=request.POST.get('email')
        C=request.POST.get('message')
        dataa = message( username = un , email = E , message = C)
        dataa.save()
    return render(request , 'work.html' )
def post (request):
    if request.method == 'POST':
        H=request.POST.get('head')
        I=request.POST.get('image')
        D=request.POST.get('deatil')
        dataa = posts( head =H , image = I , deatil = D  )
        dataa.save()
        #return redirect('post')
    return render(request , 'work.html', {'pro': posts.objects.all()})
def home(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'comment' and first(request):
            return redirect('home')
        elif action == 'contact' and contact(request):
            return redirect('home')
        elif action == 'post' and post(request):
            return redirect('home')
    context = {
        'CT': comment.objects.all(),
        'pro': posts.objects.all(),
    }
    return render(request, 'work.html', context)
def update(request , id):
    comment_id= comment.objects.get(id=id)
    if request.method=='POST':
        comment_save=CommentForm(request.POST , request.FILES , instance=comment_id)
        if comment_save.is_valid():
            comment_save.save()
            return redirect('/')
    else:
        comment_save=CommentForm(instance=comment_id)
    context ={
        "form":comment_save
    }
    return render(request , 'update.html', context)
def delate(request, id):
    comment_delate=comment.objects.get(id=id)
    if request.method=='POST':
        comment_delate.delete()
        return redirect('home')
    return render(request , 'delate.html')


        
    