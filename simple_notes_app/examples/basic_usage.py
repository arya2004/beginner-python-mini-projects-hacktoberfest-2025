#!/usr/bin/env python3
"""
简单笔记应用基础使用示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from notes_app import NotesApp

def main():
    """基础使用示例"""
    print("📝 简单笔记应用 - 基础使用示例")
    print("=" * 50)
    
    # 1. 创建应用实例
    print("\n1. 创建应用实例...")
    app = NotesApp("example_notes")
    print(f"   数据目录: {app.storage_dir}")
    
    # 2. 创建笔记
    print("\n2. 创建笔记...")
    notes_data = [
        {"title": "工作待办", "content": "完成项目报告\n准备会议材料", "tags": ["工作", "重要"]},
        {"title": "学习计划", "content": "学习Python高级特性\n完成Git教程", "tags": ["学习", "编程"]},
        {"title": "购物清单", "content": "牛奶、鸡蛋、面包、水果", "tags": ["购物", "日常"]},
        {"title": "读书笔记", "content": "《Python编程从入门到实践》第5章", "tags": ["学习", "读书"]},
        {"title": "健身计划", "content": "周一：跑步\n周三：力量训练\n周五：瑜伽", "tags": ["健康", "运动"]}
    ]
    
    created_notes = []
    for data in notes_data:
        note = app.create_note(data["title"], data["content"], data["tags"])
        created_notes.append(note)
        print(f"   创建: {note['title']}")
    
    # 3. 显示所有笔记
    print(f"\n3. 显示所有笔记 ({len(created_notes)} 个)...")
    all_notes = app.get_all_notes()
    for i, note in enumerate(all_notes, 1):
        print(f"   {i}. {note['title']}")
        print(f"      标签: {', '.join(note['tags'])}")
        print(f"      创建: {note['created_at'][:10]}")
    
    # 4. 搜索笔记
    print("\n4. 搜索笔记...")
    search_keywords = ["工作", "学习", "Python"]
    
    for keyword in search_keywords:
        results = app.search_notes(keyword)
        print(f"   搜索 '{keyword}': 找到 {len(results)} 个结果")
        for result in results:
            print(f"     - {result['title']}")
    
    # 5. 更新笔记
    print("\n5. 更新笔记...")
    if created_notes:
        first_note = created_notes[0]
        updated = app.update_note(
            first_note["id"],
            content=first_note["content"] + "\n✅ 已完成项目报告",
            tags=first_note["tags"] + ["已完成"]
        )
        print(f"   更新笔记: {updated['title']}")
        print(f"   新标签: {', '.join(updated['tags'])}")
    
    # 6. 归档笔记
    print("\n6. 归档笔记...")
    if len(created_notes) > 1:
        note_to_archive = created_notes[1]
        archived = app.archive_note(note_to_archive["id"])
        print(f"   归档笔记: {archived['title']}")
        
        # 验证归档
        active_notes = app.get_all_notes()
        all_notes_with_archived = app.get_all_notes(include_archived=True)
        print(f"   活跃笔记: {len(active_notes)} 个")
        print(f"   所有笔记（含归档）: {len(all_notes_with_archived)} 个")
    
    # 7. 导出笔记
    print("\n7. 导出笔记...")
    
    # 导出为JSON
    json_export = app.export_notes("json")
    json_file = app.storage_dir / "notes_export.json"
    with open(json_file, "w", encoding="utf-8") as f:
        f.write(json_export)
    print(f"   JSON导出: {json_file} ({len(json_export)} 字符)")
    
    # 导出为TXT
    txt_export = app.export_notes("txt")
    txt_file = app.storage_dir / "notes_export.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(txt_export)
    print(f"   TXT导出: {txt_file} ({len(txt_export)} 字符)")
    
    # 8. 统计信息
    print("\n8. 统计信息...")
    all_notes = app.get_all_notes(include_archived=True)
    tag_count = {}
    
    for note in all_notes:
        for tag in note["tags"]:
            tag_count[tag] = tag_count.get(tag, 0) + 1
    
    print(f"   总笔记数: {len(all_notes)}")
    print(f"   标签统计:")
    for tag, count in sorted(tag_count.items(), key=lambda x: x[1], reverse=True):
        print(f"     {tag}: {count} 个笔记")
    
    print("\n✅ 示例完成！")
    print(f"   数据保存在: {app.storage_dir}/")

if __name__ == "__main__":
    main()