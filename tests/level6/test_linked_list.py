"""Tests for LinkedList implementation. Gemma must write linked_list.py to pass these."""

import pytest
from linked_list import LinkedList


class TestLinkedList:
    def test_empty_list(self):
        ll = LinkedList()
        assert len(ll) == 0
        assert ll.is_empty()
        assert list(ll) == []

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert list(ll) == [1, 2, 3]
        assert len(ll) == 3

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)
        assert list(ll) == [1, 2, 3]

    def test_insert_at(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(3)
        ll.insert_at(1, 2)
        assert list(ll) == [1, 2, 3]

    def test_insert_at_beginning(self):
        ll = LinkedList()
        ll.append(2)
        ll.insert_at(0, 1)
        assert list(ll) == [1, 2]

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.append(1)
        ll.insert_at(1, 2)
        assert list(ll) == [1, 2]

    def test_insert_at_invalid_index(self):
        ll = LinkedList()
        with pytest.raises(IndexError):
            ll.insert_at(5, 1)

    def test_delete_value(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.delete(2)
        assert list(ll) == [1, 3]

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(1)
        assert list(ll) == [2]

    def test_delete_not_found(self):
        ll = LinkedList()
        ll.append(1)
        with pytest.raises(ValueError):
            ll.delete(99)

    def test_find(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        assert ll.find(20) == 1
        assert ll.find(10) == 0
        assert ll.find(30) == 2
        assert ll.find(99) == -1

    def test_get(self):
        ll = LinkedList()
        ll.append("a")
        ll.append("b")
        ll.append("c")
        assert ll.get(0) == "a"
        assert ll.get(1) == "b"
        assert ll.get(2) == "c"

    def test_get_invalid_index(self):
        ll = LinkedList()
        ll.append(1)
        with pytest.raises(IndexError):
            ll.get(5)

    def test_reverse(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()
        assert list(ll) == [3, 2, 1]

    def test_reverse_empty(self):
        ll = LinkedList()
        ll.reverse()
        assert list(ll) == []

    def test_reverse_single(self):
        ll = LinkedList()
        ll.append(1)
        ll.reverse()
        assert list(ll) == [1]

    def test_contains(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert 1 in ll
        assert 2 in ll
        assert 3 not in ll

    def test_str(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert str(ll) == "1 -> 2 -> 3 -> None"

    def test_str_empty(self):
        ll = LinkedList()
        assert str(ll) == "None"

    def test_from_list(self):
        ll = LinkedList.from_list([5, 10, 15])
        assert list(ll) == [5, 10, 15]
        assert len(ll) == 3
