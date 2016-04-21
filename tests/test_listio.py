#!/usr/bin/env python

import os
import unittest

import listio


class Test(unittest.TestCase):

    def test_read_list(self):
        TMP_FILE_PATH = '_tmp_list.txt'
        with open(TMP_FILE_PATH, 'w') as f:
            f.write(
                'First item\n'
                'second item\n'
                'foo\n'
                '# this is a comment\n'
                'bar\n'
            )
        self.assertEqual(
            listio.read_list(TMP_FILE_PATH),
            [
                'First item',
                'second item',
                'foo',
                'bar',
            ]
        )
        os.remove(TMP_FILE_PATH)

    def test_write_list(self):
        TMP_FILE_PATH = '_tmp_list.txt'
        listio.write_list(
            TMP_FILE_PATH,
            [
                'First item',
                'second item',
                'foo',
                'bar',
            ]
        )
        with open(TMP_FILE_PATH, 'r') as f:
            self.assertEqual(
                f.read(),
                'First item\n'
                'second item\n'
                'foo\n'
                'bar\n'
            )
        os.remove(TMP_FILE_PATH)

    def test_read_map(self):
        TMP_FILE_PATH = '_tmp_map.txt'
        with open(TMP_FILE_PATH, 'w') as f:
            f.write(
                'First column;"second column";3\n'
                '# this is a comment\n'
                '"next;item,";foo;bar\n'
            )
        self.assertEqual(
            list(listio.read_map(TMP_FILE_PATH)),
            [
                ['First column', 'second column', '3'],
                ['next;item,', 'foo', 'bar'],
            ]
        )
        os.remove(TMP_FILE_PATH)

    def test_write_map(self):
        TMP_FILE_PATH = '_tmp_map.txt'
        listio.write_map(
            TMP_FILE_PATH,
            [
                ['First column', 'second column', '3'],
                ['next;item,', 'foo', 'bar'],
            ]
        )
        with open(TMP_FILE_PATH, 'r') as f:
            self.assertEqual(
                f.read(),
                'First column;second column;3\n'
                '"next;item,";foo;bar\n'
            )
        os.remove(TMP_FILE_PATH)


if __name__ == '__main__':
    unittest.main()
