from myllm.MyApi import geminiModel

def test():
    model = geminiModel()
    response = model.generate_content("한국의 수도는 어디야")
    print(response.text)


if __name__ == '__main__':
    test()