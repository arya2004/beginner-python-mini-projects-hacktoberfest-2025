#!/usr/bin/env python3
"""
简单笔记应用的单元测试
"""

import unittest
import os
import tempfile
import shutil
from notes_app import NotesApp

class TestNotesApp(unittest.TestCase):
    """测试NotesApp类"""
    
    def setUp(self):
        """测试前准备"""
        self.test_dir = tempfile.mkdtemp()
        self.app = NotesApp(storage_dir=self.test_dir)
    
    def tearDown(self):
        """测试后清理"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_create_note(self):
        """测试创建笔记"""
        note = self.app.create_note("测试标题", "测试内容", ["测试"])
        
        self.assertEqual(note["title"], "测试标题")
        self.assertEqual(note["content"], "测试内容")
        self.assertEqual(note["tags"], ["测试"])
        self.assertFalse(note["is_archived"])
        
        # 验证笔记已保存
        notes = self.app.get_all_notes()
        self.assertEqual(len(notes), 1)
    
    def test_get_note(self):
        """测试获取笔记"""
        note = self.app.create_note("测试", "内容", ["标签"])
        retrieved = self.app.get_note(note["id"])
        
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved["title"], "测试")
        self.assertEqual(retrieved["id"], note["id"])
    
    def test_get_note_not_found(self):
        """测试获取不存在的笔记"""
        result = self.app.get_note(999)
        self.assertIsNone(result)
    
    def test_update_note(self):
        """测试更新笔记"""
        note = self.app.create_note("原标题", "原内容", ["原标签"])
        
        updated = self.app.update_note(
            note["id"],
            title="新标题",
            content="新内容",
            tags=["新标签"]
        )
        
        self.assertIsNotNone(updated)
        self.assertEqual(updated["title"], "新标题")
        self.assertEqual(updated["content"], "新内容")
        self.assertEqual(updated["tags"], ["新标签"])
    
    def test_delete_note(self):
        """测试删除笔记"""
        note1 = self.app.create_note("笔记1", "内容1")
        note2 = self.app.create_note("笔记2", "内容2")
        
        self.assertEqual(len(self.app.get_all_notes()), 2)
        
        self.app.delete_note(note1["id"])
        
        notes = self.app.get_all_notes()
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0]["id"], note2["id"])
    
    def test_search_notes(self):
        """测试搜索笔记"""
        self.app.create_note("Python学习", "学习Python编程", ["编程", "学习"])
        self.app.create_note("购物清单", "牛奶、鸡蛋", ["购物"])
        self.app.create_note("项目计划", "Python项目开发", ["项目", "Python"])
        
        # 搜索标题
        results = self.app.search_notes("Python")
        self.assertEqual(len(results), 2)
        
        # 搜索内容
        results = self.app.search_notes("牛奶")
        self.assertEqual(len(results), 1)
        
        # 搜索标签
        results = self.app.search_notes("购物")
        self.assertEqual(len(results), 1)
    
    def test_archive_note(self):
        """测试归档笔记"""
        note = self.app.create_note("测试", "内容")
        
        self.assertFalse(note["is_archived"])
        
        archived = self.app.archive_note(note["id"])
        self.assertTrue(archived["is_archived"])
        
        # 归档后不应出现在普通列表中
        notes = self.app.get_all_notes()
        self.assertEqual(len(notes), 0)
        
        # 但应出现在包含归档的列表中
        notes_with_archived = self.app.get_all_notes(include_archived=True)
        self.assertEqual(len(notes_with_archived), 1)
    
    def test_export_notes(self):
        """测试导出笔记"""
        self.app.create_note("笔记1", "内容1", ["标签1"])
        self.app.create_note("笔记2", "内容2", ["标签2"])
        
        # 导出为JSON
        json_export = self.app.export_notes("json")
        self.assertIsInstance(json_export, str)
        self.assertIn("笔记1", json_export)
        
        # 导出为TXT
        txt_export = self.app.export_notes("txt")
        self.assertIsInstance(txt_export, str)
        self.assertIn("笔记1", txt_export)
        self.assertIn("内容2", txt_export)
    
    def test_persistence(self):
        """测试数据持久化"""
        # 创建应用并添加笔记
        app1 = NotesApp(storage_dir=self.test_dir)
        note = app1.create_note("持久化测试", "测试内容")
        
        # 创建新应用实例，应该能读取到数据
        app2 = NotesApp(storage_dir=self.test_dir)
        notes = app2.get_all_notes()
        
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0]["title"], "持久化测试")

class TestNotesAppIntegration(unittest.TestCase):
    """集成测试"""
    
    def test_complete_workflow(self):
        """测试完整工作流程"""
        app = NotesApp(storage_dir=tempfile.mkdtemp())
        
        # 1. 创建多个笔记
        note1 = app.create_note("工作", "完成项目", ["工作", "重要"])
        note2 = app.create_note("学习", "学习Python", ["学习", "编程"])
        note3 = app.create_note("购物", "买牛奶", ["购物", "日常"])
        
        # 2. 验证创建
        self.assertEqual(len(app.get_all_notes()), 3)
        
        # 3. 搜索
        work_notes = app.search_notes("工作")
        self.assertEqual(len(work_notes), 1)
        
        # 4. 更新
        app.update_note(note2["id"], content="学习Python和Git")
        
        # 5. 归档
        app.archive_note(note3["id"])
        
        # 6. 验证归档
        self.assertEqual(len(app.get_all_notes()), 2)
        
        # 7. 删除
        app.delete_note(note1["id"])
        
        # 8. 最终验证
        final_notes = app.get_all_notes()
        self.assertEqual(len(final_notes), 1)
        self.assertEqual(final_notes[0]["title"], "学习")
        
        # 9. 导出
        export = app.export_notes("json")
        self.assertIn("学习", export)

def run_tests():
    """运行所有测试"""
    print("🧪 运行简单笔记应用测试...")
    print("=" * 50)
    
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 添加测试类
    suite.addTests(loader.loadTestsFromTestCase(TestNotesApp))
    suite.addTests(loader.loadTestsFromTestCase(TestNotesAppIntegration))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 50)
    print(f"测试结果: {result.testsRun} 个测试")
    print(f"通过: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"失败: {len(result.failures)}")
    print(f"错误: {len(result.errors)}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    if success:
        print("✅ 所有测试通过！")
    else:
        print("❌ 测试失败，请检查代码")