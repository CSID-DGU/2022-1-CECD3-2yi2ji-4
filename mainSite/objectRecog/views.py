from django.shortcuts import render
import requests
import json
import pyttsx3


def barcode(request):
    return render(request, 'barcode.html')


def send(request):
    if request.method == 'POST':
        data = request.POST.get('result')
        print(data)

        b_code = data
        url = 'http://openapi.foodsafetykorea.go.kr/api/ac73ac10d9fd494c90f2/C005/json/1/5/BAR_CD='+ b_code
        response = requests.get(url)
        contents = response.text
        dic = json.loads(contents)
        resultString = ""

        if (dic['C005']['total_count']=='0'):
            engine = pyttsx3.init()
            if (engine._inLoop):
                engine.endLoop()

            engine.setProperty('rate', 110)
            resultString = "입력하신 바코드의 정보를 찾을 수 없습니다."
            engine.say(resultString)
            engine.save_to_file(resultString, 'static/barcode.mp3')
            engine.runAndWait()
            engine = None

        else:
            result = dic['C005']['row'][0]
            BSSH_NM = result['BSSH_NM'].replace('주', '')
            engine = pyttsx3.init()
            if (engine._inLoop):
                engine.endLoop()

            engine.setProperty('rate', 110)
            resultString = '입력하신 바코드의 제품 명은 '+result['PRDLST_NM'] + ', 제품 종류는 '+ result['PRDLST_DCNM'] + ', 제조사는 '+ BSSH_NM + ', 입니다'
            engine.say(resultString)
            engine.save_to_file(resultString, 'static/barcode.mp3')
            engine.runAndWait()
        return render(request, 'barcode.html')