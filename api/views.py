from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. Api index")

def keyGeneration(request):
  print(request.GET.get("keyGenAlg"))
  # 拿到前端传来的参数
  # 使用对应算法，然后返回结果
  return HttpResponse("key Generation hahha")