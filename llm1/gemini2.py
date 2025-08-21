from PIL import Image

from myllm.MyApi import geminiModel

def test():
    img = Image.open("img/img.png")
    model = geminiModel()
    response = model.generate_content(("사진에 나온 오리는 뭘 먹어", img))
    print(response.text)

if __name__=='__main__':
    test()