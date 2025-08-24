import os
import sys


def create_project(name):
    os.makedirs(name, exist_ok=True)

    py_path = os.path.join(name, f"{name}.py")
    txt_path = os.path.join(name, f"{name}.txt")

    if not os.path.exists(txt_path):
        with open(txt_path, "w", encoding="utf-8") as f:
            pass

    if not os.path.exists(py_path):
        with open(py_path, "w", encoding="utf-8") as f:
            f.write(f'import sys; sys.stdin = open("{name}.txt")\n')

    ans.append(f"✅ '{name}' 폴더와 {name}.py, {name}.txt 생성 완료!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        ans.append("⚠️ 사용법: python make_files.py <폴더이름>")
    else:
        folder_name = sys.argv[1]  # 명령줄 인자에서 이름 가져오기
        create_project(folder_name)