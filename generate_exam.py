import csv

input_csv = "algorithm_interview.csv"     # 입력 CSV 파일명
output_md = "interview.md"      # 출력 Markdown 파일명

# 난이도별 색상 지정
difficulty_color = {
    "초급": "#2ecc71",   # green
    "중급": "#e67e22",   # orange
    "고급": "#e74c3c"    # red
}

template = """
### {index}. {question}

**난이도:** <span style="color:{color}; font-weight:bold;">{difficulty}</span>

<form class="inline-answer">
  <input type="text" placeholder="내 답 입력…" />
</form>

<details class="answer-box">
<summary>답변 예시</summary>
<div markdown="1">

> {answer}
</div>
</details>

<br/><br/>
___
"""

def csv_to_markdown(input_csv, output_md):
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        md_output = []

        for row in reader:
            idx = row["문제 번호"].strip()
            question = row["질문"].strip()
            difficulty = row["난이도 (초/중/고)"].strip()
            answer = row["답변 예시"].strip()

            color = difficulty_color.get(difficulty, "#000000")  # 기본 검정

            md_output.append(
                template.format(
                    index=idx,
                    question=question,
                    difficulty=difficulty,
                    color=color,
                    answer=answer
                )
            )

    with open(output_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_output))

    print(f"Markdown 파일 생성 완료: {output_md}")


if __name__ == "__main__":
    csv_to_markdown(input_csv, output_md)
