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
