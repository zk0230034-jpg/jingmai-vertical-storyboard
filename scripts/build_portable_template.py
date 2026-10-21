"""Build the standalone Jingmai prompt from the skill's canonical references."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCE_NAMES = (
    "workflow.md",
    "director-plan-compiler.md",
    "beat-coverage.md",
    "dramatic-rhythm.md",
    "narrative-shot-selection.md",
    "pacing-and-shot-density.md",
    "shot-chain.md",
    "cinematic-language.md",
    "integrated-shot-design.md",
    "camera-movement-lexicon.md",
    "shot-size-angle-composition.md",
    "focus-light-sound.md",
    "performance-direction.md",
    "action-choreography.md",
    "martial-arts-vocabulary.md",
    "vfx-design.md",
    "method-examples.md",
    "output-contract.md",
    "directing-and-revision.md",
    "quality-gates.md",
    "counterfactual-tests.md",
)

INTRO = """# 镜脉竖屏短剧分镜提示词模板 V10.0｜导演决策与连续镜头版

将本模板完整交给目标AI，再提供真实剧本和已确认的集数、模型、制作方向、导演方案与重点。AI须把剧本视为唯一剧情事实源，把本文视为工作规则。本文没有可直接复制到作品的人物、招式、台词或能力设定；任何案例只用来理解方法。缺少剧本时仅邀请用户提供，不虚构分析。

目标是可表演、可剪辑、可供视频模型执行的镜头。V10.0按“原稿拍点覆盖→导演方案与节奏曲线→人物和空间行动→影视要素联合选择→相邻镜头接力→容量与删镜复核”工作。不能漏掉或重复关键剧情，也不能让一串漂亮的单镜变成无法连续剪辑的段落。专业术语必须附可见执行，镜头语言为人物、信息与动作服务。用户已给出的选择不要重问，未回复不算确认。以下知识库是候选工具，不是每Part必须用满的清单；普通文戏不套动作或特效清单，普通动作不为炫技增添不存在的流派和能力。镜头数由故事负荷与可读时间决定，不把某个区间当作短剧标准答案。
"""


def build() -> str:
    sections = [INTRO.rstrip()]
    for name in REFERENCE_NAMES:
        source = ROOT / "references" / name
        sections.append(source.read_text(encoding="utf-8").strip())
    return "\n\n---\n\n".join(sections) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Target Markdown file")
    args = parser.parse_args()
    target = args.output.resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build(), encoding="utf-8", newline="\n")
    print(f"Built {target}")


if __name__ == "__main__":
    main()
