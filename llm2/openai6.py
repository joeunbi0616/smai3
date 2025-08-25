import urllib

from myllm.MyApi import openAiModel, makeMsg, openAiModelArg


def test(prompt):
    openModel = openAiModel()
    response = openModel.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    print(image_url)
    imgName = "img/dogncat.png"
    urllib.request.urlretrieve(image_url, imgName)

if __name__=='__main__':
    prompt="흰색 강아지와 흰색 고양이 사진 만들어줘"
    test(prompt)