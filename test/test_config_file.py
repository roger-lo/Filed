
from unittest.mock import MagicMock, patch

from src import filed


@patch('src.filed.path')
def test_basic(p_path):
    fd = ['source:destination:.*']

    m_expanduser = MagicMock()
    m_expanduser.side_effect = (lambda x: x)
    p_path.expanduser = m_expanduser

    rules = filed.parse_config_file(fd)

    assert len(rules) == 1
    assert rules[0].src == 'source'
    assert rules[0].dst == 'destination'
    assert rules[0].reg == '.*'
