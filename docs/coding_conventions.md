# viewKit コーディング規約

基本方針として、 PEP8 に準拠します。

ただし、1行の文字数など、一部のルールを緩和しています。

---

## **1. 命名規則**

Python では **snake_case を基本** とし、クラスや定数など特定のものには別のケースを使います。

- **変数・関数**: `snake_case`
  ```python
  def get_user_data():
      user_name = "Alice"
  ```

- **クラス**: `PascalCase`（または `CapWords`）
  ```python
  class UserProfile:
      pass
  ```

- **モジュール・パッケージ**: `snake_case`（ただし短めに）
  ```python
  import user_profile
  ```

- **定数**: `SCREAMING_SNAKE_CASE`
  ```python
  MAX_CONNECTIONS = 100
  ```

- **非公開変数・関数**: `_single_leading_underscore`
  ```python
  _internal_variable = "hidden"
  ```

---

## **2. インデントと空白**

- **インデントは 4 スペース**
  ```python
  def example_function():
      print("Hello, world!")
  ```

- **行末の空白を避ける**
- **演算子の前後にスペースを入れる**
  ```python
  x = 10 + 20  # OK
  y=10+20      # NG
  ```

---

## **3. コメントとドキュメンテーション**

### **(1) 通常のコメント**

- **`#` を使い、1行コメントを入れる**
  ```python
  # ここで値を更新
  value = 42
  ```

### **(2) Docstring**

- **関数やクラスには `"""` で始まる Docstring を記述**
  ```python
  def add(x, y):
      """2つの数値を加算して返す"""
      return x + y
  ```

---

## **4. 文字列の扱い**
- 文字列は ダブルクォート `" "` にを統一**
  ```python
  message = "Hello, world!"
  ```

- 長い文字列は `"""`（または `'''`）を使用
  ```python
  long_text = """この文字列は
  複数行にわたる
  文字列です。"""
  ```

---

## **5. 関数とメソッド**

- **1行の長さには制限を付けないが、適切な長さで改行することを推奨**
- **引数が多い場合、改行して整形**
  ```python
  def my_function(
      param1: str,
      param2: int,
      param3: list
  ) -> None:
      pass
  ```

---

## **6. クラス設計**
- **`__init__` で初期化**
  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  ```

- **メソッドは1行空ける**
  ```python
  class User:
      def login(self):
          pass

      def logout(self):
          pass
  ```

---

## **7. 型ヒント (Type Hints)**
Python 3.5 以降では **型アノテーション** を使うのが推奨されます。 viewKit では必須にはしませんが、書けるなら書いた方がいいかも。

```python
def greet(name: str) -> str:
    return "Hello, " + name
```

---

## **8. 例外処理**
- **`try-except` を適切に使う**
  ```python
  try:
      value = int("abc")
  except ValueError as e:
      print(f"変換エラー: {e}")
  ```

---
