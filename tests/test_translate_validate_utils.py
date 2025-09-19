import unittest

from scripts.translation.translate_validate_utils import (
    check_prohibited_zh_terms,
    check_yin_wang_mistranslation,
)


class TestTranslateValidateUtils(unittest.TestCase):
    def test_yin_wang_mistranslation_raises_on_yin_king(self):
        original = "Notes about Yin Wang and his blog."
        translated = "关于阴王及其博客的笔记。"
        with self.assertRaises(RuntimeError):
            check_yin_wang_mistranslation(original, translated, "zh")

    def test_yin_wang_mistranslation_raises_on_wang_yin(self):
        original = "A paper by Yin Wang about compilers."
        translated = "王寅关于编译器的论文。"
        with self.assertRaises(RuntimeError):
            check_yin_wang_mistranslation(original, translated, "zh")

    def test_yin_wang_correct_translation_passes(self):
        original = "Interview with Yin Wang"
        translated = "与王垠的访谈"
        # Should not raise
        check_yin_wang_mistranslation(original, translated, "zh")

    def test_non_zh_target_passes(self):
        original = "Interview with Yin Wang"
        translated = "Entrevista con Yin Wang"
        # Non-Chinese target should not trigger the check
        check_yin_wang_mistranslation(original, translated, "es")

    def test_original_without_name_passes_even_if_cn_words_present(self):
        original = "Unrelated content about names."
        translated = "这篇文章提到了阴王与王寅。"
        # Original doesn't contain 'Yin Wang'; should not raise
        check_yin_wang_mistranslation(original, translated, "zh")

    def test_prohibited_zhiwei_raises_for_chinese(self):
        with self.assertRaises(RuntimeError):
            check_prohibited_zh_terms("包含志炜的翻译。", "zh")

    def test_prohibited_zhiwei_allows_other_languages(self):
        # Should not raise for non-Chinese targets even if the phrase appears
        check_prohibited_zh_terms("包含志炜的翻译。", "es")


if __name__ == "__main__":
    unittest.main()
