#coding:utf-8
from django.shortcuts import render
from models import Question,Choice
# Create your views here.
def index(req):
    #取出数据库Question的成员，question_text/ pubtime
    ques=Question.objects.all()
    con={'Ques':ques}
    return render(req,'index.html',con)
def show(req,id):
    # 根据问题的id(喜欢看什么电影)
    que=Question.objects.get(pk=id)
    # 根据外键获取当前问题的选项表单
    choice_object=que.choice_set
    #去除表单选项的内容（科幻、爱情、动作）
    chos=choice_object.all()
    # 承接上下文，字典，传递参数问题还有表单内容
    con={'Ques':que,'Chos':chos}
    return render(req,'show.html',con)

def showaction(req,id):
    # 获取Question的一个对象（ question_text和pubtime）比如：今天喜欢看什么电影和Aug. 2, 2017, 2:03 p.m.
    que=Question.objects.get(pk=id)
    #获取该问题对应的表单选项
    choice_biao=que.choice_set
    #获取表单所有的对象 （科幻、动作、爱情）
    chos=choice_biao.all()
    # 将id字符串转化为int类型
    k=int(id)
    if (k)%2==0:

        #获取表单form中选中的value值 list列表
        nums=req.POST.getlist('choice')

        if nums==[]:


            #渲染到show.html页面，和上面show函数相应的渲染相同，保留当前页面，再添加一个错误提示
            return render(req,'show.html',{'Chos':chos,'Ques':que,'myError':'please check one!'})
            #获得Choice表单选项的一个对象（choicetext和vote）比如：科幻  和  vote=0
        else:
            for num in nums:
                target=choice_biao.get(pk=num)
                target.vote+=1
                # 将vote的值存储到内存中
                target.save()
            #获取所有的对象
            que=Question.objects.get(pk=id)
            return render(req,'showresult.html',{'Que':que})
    else:
        try:
          num=req.POST['choice']
        except (KeyError,Choice.DoesNotExist):
           return render(req,'show.html',{'Chos':chos,'Ques':que,'myERROR':'你没有选中选项，重选'})
        for x in num:
            target=choice_biao.get(pk=x)
            target.vote+=1
            target.save()
        que=Question.objects.get(pk=id)
        return render(req,'showresult.html',{'Que':que})




