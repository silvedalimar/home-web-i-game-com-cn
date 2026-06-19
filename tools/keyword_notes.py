from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SAMPLE_URL = "https://home-web-i-game.com.cn"
CORE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    keyword: str
    note: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[datetime] = None
    url: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.url is None:
            self.url = SAMPLE_URL


def format_notes_as_section(notes: List[KeywordNote]) -> str:
    """生成格式化输出，适合在控制台或日志中展示"""
    output_parts = []
    separator = "-" * 48

    for idx, note in enumerate(notes, start=1):
        block = [
            separator,
            f"笔记 #{idx}",
            f"关键词: {note.keyword}",
            f"笔记内容: {note.note}",
            f"标签: {', '.join(note.tags) if note.tags else '无'}",
            f"创建时间: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"关联URL: {note.url}",
        ]
        output_parts.extend(block)

    output_parts.append(separator)
    return "\n".join(output_parts)


def generate_example_notes() -> List[KeywordNote]:
    """生成一组示例笔记，包含核心关键词和关联URL"""
    notes = [
        KeywordNote(
            keyword=CORE_KEYWORD,
            note="用户登录后可通过活动界面领取每日奖励。",
            tags=["活动", "奖励", "每日"],
            url=SAMPLE_URL,
        ),
        KeywordNote(
            keyword="怀旧回忆",
            note="经典游戏关卡复刻，大量老玩家回归。",
            tags=["怀旧", "经典", "活动"],
        ),
        KeywordNote(
            keyword="新手指南",
            note="新注册用户自动加入新手引导任务链。",
            tags=["新手", "引导", "教程"],
        ),
        KeywordNote(
            keyword=CORE_KEYWORD,
            note="社交分享功能上线，邀请好友可获得额外积分。",
            tags=["社交", "分享", "积分"],
            url=SAMPLE_URL,
        ),
    ]
    return notes


def filter_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """返回包含指定关键词的笔记列表（不区分大小写）"""
    return [note for note in notes if note.keyword.lower() == keyword.lower()]


def display_notes_summary(notes: List[KeywordNote]) -> None:
    """简单打印笔记摘要"""
    if not notes:
        print("没有符合条件的笔记。")
        return

    print(f"共找到 {len(notes)} 条笔记：")
    for note in notes:
        tags_str = f"[{', '.join(note.tags)}]" if note.tags else ""
        print(f"  · {note.keyword}：{note.note[:50]}{'...' if len(note.note) > 50 else ''} {tags_str}")


def main():
    all_notes = generate_example_notes()

    print("=== 全部笔记 ===")
    print(format_notes_as_section(all_notes))

    print("\n=== 仅显示核心关键词笔记 ===")
    core_notes = filter_notes_by_keyword(all_notes, CORE_KEYWORD)
    display_notes_summary(core_notes)

    print("\n=== 测试：不存在的关键词 ===")
    no_match = filter_notes_by_keyword(all_notes, "不存在的关键词")
    display_notes_summary(no_match)


if __name__ == "__main__":
    main()