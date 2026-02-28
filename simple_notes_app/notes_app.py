#!/usr/bin/env python3
"""
简单笔记应用 - 为GitHub任务准备
支持文件存储的笔记管理应用
"""

import os
import json
import datetime
from pathlib import Path

class NotesApp:
    """笔记应用核心类"""
    
    def __init__(self, storage_dir="notes_data"):
        """初始化应用"""
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        self.notes_file = self.storage_dir / "notes.json"
        self.notes = self._load_notes()
    
    def _load_notes(self):
        """加载笔记数据"""
        if self.notes_file.exists():
            try:
                with open(self.notes_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _save_notes(self):
        """保存笔记数据"""
        with open(self.notes_file, 'w', encoding='utf-8') as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)
    
    def create_note(self, title, content, tags=None):
        """创建新笔记"""
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().isoformat()
        
        note = {
            "id": note_id,
            "title": title,
            "content": content,
            "tags": tags or [],
            "created_at": timestamp,
            "updated_at": timestamp,
            "is_archived": False
        }
        
        self.notes.append(note)
        self._save_notes()
        return note
    
    def get_note(self, note_id):
        """获取单个笔记"""
        for note in self.notes:
            if note["id"] == note_id:
                return note
        return None
    
    def get_all_notes(self, include_archived=False):
        """获取所有笔记"""
        if include_archived:
            return self.notes
        return [note for note in self.notes if not note["is_archived"]]
    
    def update_note(self, note_id, title=None, content=None, tags=None):
        """更新笔记"""
        for note in self.notes:
            if note["id"] == note_id:
                if title is not None:
                    note["title"] = title
                if content is not None:
                    note["content"] = content
                if tags is not None:
                    note["tags"] = tags
                note["updated_at"] = datetime.datetime.now().isoformat()
                self._save_notes()
                return note
        return None
    
    def delete_note(self, note_id):
        """删除笔记"""
        self.notes = [note for note in self.notes if note["id"] != note_id]
        self._save_notes()
        return True
    
    def archive_note(self, note_id):
        """归档笔记"""
        for note in self.notes:
            if note["id"] == note_id:
                note["is_archived"] = True
                note["updated_at"] = datetime.datetime.now().isoformat()
                self._save_notes()
                return note
        return None
    
    def search_notes(self, keyword):
        """搜索笔记"""
        results = []
        keyword_lower = keyword.lower()
        
        for note in self.notes:
            if (keyword_lower in note["title"].lower() or 
                keyword_lower in note["content"].lower() or
                any(keyword_lower in tag.lower() for tag in note["tags"])):
                results.append(note)
        
        return results
    
    def export_notes(self, format="json"):
        """导出笔记"""
        if format == "json":
            return json.dumps(self.notes, ensure_ascii=False, indent=2)
        elif format == "txt":
            output = []
            for note in self.notes:
                output.append(f"标题: {note['title']}")
                output.append(f"创建时间: {note['created_at']}")
                output.append(f"内容: {note['content']}")
                output.append(f"标签: {', '.join(note['tags'])}")
                output.append("-" * 40)
            return "\n".join(output)
        return ""

def main():
    """主函数 - 演示应用功能"""
    print("📝 简单笔记应用演示")
    print("=" * 40)
    
    # 创建应用实例
    app = NotesApp()
    
    # 演示功能
    print("\n1. 创建笔记...")
    note1 = app.create_note(
        "购物清单",
        "牛奶、鸡蛋、面包、水果",
        ["购物", "日常"]
    )
    print(f"   创建笔记: {note1['title']}")
    
    note2 = app.create_note(
        "项目想法",
        "开发一个智能笔记应用，支持Markdown和标签",
        ["项目", "开发", "想法"]
    )
    print(f"   创建笔记: {note2['title']}")
    
    print("\n2. 获取所有笔记...")
    notes = app.get_all_notes()
    print(f"   共有 {len(notes)} 个笔记")
    
    print("\n3. 搜索笔记...")
    results = app.search_notes("项目")
    print(f"   搜索'项目'找到 {len(results)} 个结果")
    
    print("\n4. 更新笔记...")
    updated = app.update_note(
        note1["id"],
        content="牛奶、鸡蛋、面包、水果、蔬菜"
    )
    print(f"   更新笔记内容")
    
    print("\n5. 导出笔记...")
    export_data = app.export_notes("txt")
    print(f"   导出成功，长度: {len(export_data)} 字符")
    
    print("\n✅ 演示完成！")
    print(f"   数据保存在: {app.storage_dir}/")
    
    # 显示使用说明
    print("\n📖 使用说明:")
    print("   1. 创建笔记: app.create_note(title, content, tags)")
    print("   2. 获取笔记: app.get_note(id) 或 app.get_all_notes()")
    print("   3. 搜索笔记: app.search_notes(keyword)")
    print("   4. 更新笔记: app.update_note(id, title, content, tags)")
    print("   5. 删除笔记: app.delete_note(id)")
    print("   6. 导出笔记: app.export_notes(format='json' 或 'txt')")

if __name__ == "__main__":
    main()