from PIL import Image

from myllm.MyApi import geminiModel

def test():
    img = Image.open("img/dog.png")
    model = geminiModel()
    response = model.generate_content(["제시한 이미지에 있는 강아지와 고양이의 종이 어떤 종이야",img])
    print(response.text)

if __name__ == '__main__':
    test()