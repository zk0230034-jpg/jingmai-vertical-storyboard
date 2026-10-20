"""Check mechanical storyboard structure; it does not judge directing quality."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


PART_RE = re.compile(r"^#{0,4}\s*Part\s*(\d+)\s*[｜|·]", re.I)
SHOT_RE = re.compile(r"^#{0,5}\s*镜头\s*(\d+)\s*[｜|]?")
DURATION_RE = re.compile(r"建议总时长\s*[：:]\s*约?\s*(\d+)\s*秒")
FIELD_NAMES = ("画面与表演", "台词", "环境音效", "衔接")
HEADER_NAMES = ("【人物引用】", "【场景引用】", "【重要道具】", "【开场空间与状态】", "【风格前缀】")


@dataclass
class Shot:
    number: int
    start: int
    lines: list[tuple[int, str]] = field(default_factory=list)


@dataclass
class Part:
    number: int
    start: int
    header: list[tuple[int, str]] = field(default_factory=list)
    shots: list[Shot] = field(default_factory=list)
    end: list[tuple[int, str]] = field(default_factory=list)


def parse(text: str) -> list[Part]:
    parts: list[Part] = []
    current_part: Part | None = None
    current_shot: Shot | None = None
    ended = False
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        part_match = PART_RE.match(line)
        if part_match:
            current_part = Part(int(part_match.group(1)), line_no)
            parts.append(current_part)
            current_shot = None
            ended = False
            continue
        if current_part is None:
            continue
        shot_match = SHOT_RE.match(line)
        if shot_match:
            current_shot = Shot(int(shot_match.group(1)), line_no)
            current_part.shots.append(current_shot)
            ended = False
            continue
        if line.startswith("【结束状态】"):
            current_shot = None
            ended = True
        if ended:
            current_part.end.append((line_no, line))
        elif current_shot is not None:
            current_shot.lines.append((line_no, line))
        else:
            current_part.header.append((line_no, line))
    return parts


def validate(parts: list[Part], model: str, expected_parts: int | None) -> list[str]:
    errors: list[str] = []
    if not parts:
        return ["未找到 Part 标题。"]
    if expected_parts is not None and len(parts) != expected_parts:
        errors.append(f"预计 {expected_parts} 个 Part，实际 {len(parts)} 个。")
    limit = 15 if model == "2.0" else 30
    for index, part in enumerate(parts, 1):
        label = f"Part {part.number}（第 {part.start} 行）"
        if part.number != index:
            errors.append(f"{label}：Part 编号应为 {index}。")
        header_text = "\n".join(line for _, line in part.header)
        duration = DURATION_RE.search(header_text)
        if not duration:
            errors.append(f"{label}：缺少建议总时长。")
        elif int(duration.group(1)) > limit:
            errors.append(f"{label}：声明 {duration.group(1)} 秒，超过 Seedance {model} 的工作流上限 {limit} 秒。")
        for header in HEADER_NAMES:
            if header not in header_text:
                errors.append(f"{label}：缺少 {header}。")
        if not part.shots:
            errors.append(f"{label}：没有镜头。")
        if not any(line.startswith("【结束状态】") for _, line in part.end):
            errors.append(f"{label}：缺少【结束状态】。")
        for expected_shot, shot in enumerate(part.shots, 1):
            shot_label = f"{label} 镜头 {shot.number}（第 {shot.start} 行）"
            if shot.number != expected_shot:
                errors.append(f"{shot_label}：镜头编号应为 {expected_shot}。")
            body = "\n".join(line for _, line in shot.lines)
            for field_name in FIELD_NAMES:
                count = len(re.findall(rf"^{re.escape(field_name)}[：:]", body, re.M))
                if count != 1:
                    errors.append(f"{shot_label}：{field_name} 字段应恰好出现一次，实际 {count} 次。")
            for line_no, line in shot.lines:
                if re.match(r"^(?:表演|光影|构图与焦点|景别[・·]视角|Seedance Prompt)[：:]", line):
                    errors.append(f"{shot_label} 第 {line_no} 行：出现额外逐镜字段。")
                if re.search(r"\d{1,2}\s*[-—–~至]\s*\d{1,2}\s*秒|\d{1,2}:\d{2}", line):
                    errors.append(f"{shot_label} 第 {line_no} 行：出现逐镜时长或时间码。")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Storyboards in Markdown")
    parser.add_argument("--model", choices=("2.0", "2.5"), required=True)
    parser.add_argument("--expected-parts", type=int)
    args = parser.parse_args()
    parts = parse(args.source.read_text(encoding="utf-8"))
    errors = validate(parts, args.model, args.expected_parts)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"结构检查通过：{len(parts)} 个 Part，{sum(len(part.shots) for part in parts)} 镜。")
    print("仍须人工核对原稿忠实、动作可拍性、特效一致性与台词容量。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
