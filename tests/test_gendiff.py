from gendiff.core import generate_diff


def test_generate_diff_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = '''    common: {
    + follow: False
      setting1: Value 1
    - setting2: 200
    - setting3: True
    + setting3: None
    + setting4: blah blah
    + setting5: {'key5': 'value5'}
      setting6: {
        doge: {
        - wow: 
        + wow: so much
        }
        key: value
      + ops: vops
      }
    }
    group1: {
    - baz: bas
    + baz: bars
      foo: bar
    - nest: {'key': 'value'}
    + nest: str
    }
  - group2: {'abc': 12345, 'deep': {'id': 45}}
  + group3: {'deep': {'id': {'number': 45}}, 'fee': 100500}'''
    actual = generate_diff(file1, file2)
    assert actual == expected


def test_generate_diff_yaml():
    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'
    expected = '''    follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True'''
    actual = generate_diff(file1, file2)
    assert actual == expected


def test_generate_diff_plain():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    actual = generate_diff(file1, file2, 'plain')
    assert actual == expected


def test_generate_diff_json_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = """[
    {
        "key": "common",
        "type": "nested",
        "children": [
            {
                "key": "follow",
                "type": "added",
                "value": false
            },
            {
                "key": "setting1",
                "type": "unchanged",
                "value": "Value 1"
            },
            {
                "key": "setting2",
                "type": "removed",
                "value": 200
            },
            {
                "key": "setting3",
                "type": "changed",
                "old_value": true,
                "new_value": null
            },
            {
                "key": "setting4",
                "type": "added",
                "value": "blah blah"
            },
            {
                "key": "setting5",
                "type": "added",
                "value": {
                    "key5": "value5"
                }
            },
            {
                "key": "setting6",
                "type": "nested",
                "children": [
                    {
                        "key": "doge",
                        "type": "nested",
                        "children": [
                            {
                                "key": "wow",
                                "type": "changed",
                                "old_value": "",
                                "new_value": "so much"
                            }
                        ]
                    },
                    {
                        "key": "key",
                        "type": "unchanged",
                        "value": "value"
                    },
                    {
                        "key": "ops",
                        "type": "added",
                        "value": "vops"
                    }
                ]
            }
        ]
    },
    {
        "key": "group1",
        "type": "nested",
        "children": [
            {
                "key": "baz",
                "type": "changed",
                "old_value": "bas",
                "new_value": "bars"
            },
            {
                "key": "foo",
                "type": "unchanged",
                "value": "bar"
            },
            {
                "key": "nest",
                "type": "changed",
                "old_value": {
                    "key": "value"
                },
                "new_value": "str"
            }
        ]
    },
    {
        "key": "group2",
        "type": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "key": "group3",
        "type": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]"""

    actual = generate_diff(file1, file2, format_name='json')
    print("ACTUAL RESULT:", actual)    
    assert actual == expected
