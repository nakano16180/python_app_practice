# json モジュールのインポート
import json
import pprint

def write_json():
    # JSON の書き出し用のサンプルオブジェクト
    data = {
        'title': 'JSONの読み書き',
        'author': 'Crane & to. 株式会社',
        'items': [
            {
                'title': 'Hellow JSON',
                'description': 'まずJSONについてを学びましょう'
            },
            {
                'title': 'PythonでJSON',
                'description': 'PythonでJSONを読み書きする方法を学びましょう'
            }
        ]
    }
    
    # Pythonオブジェクトをファイル書き込み
    savepath = 'data/sample.json'
    with open(savepath, 'w') as outfile:
        json.dump(data, outfile)
    
    # Pythonオブジェクトを文字列に変換
    json_str = json.dumps(data)
    pprint.pprint(json_str)

def read_json():
    try:
        # ローカルJSONファイルの読み込み
        with open('data/sample.json', 'r') as f:
            data = json.load(f)
            pprint.pprint(data)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

write_json()
read_json()