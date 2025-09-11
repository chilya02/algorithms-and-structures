import pytest
from circdeque import CircularDeque

def test_comprehensive_functionality():
    deque = CircularDeque(4, push_force=True)
    
    deque.push_front(1)
    deque.push_back(2)
    deque.push_front(0)
    deque.push_back(3)
    
    assert deque.size() == 4
    assert deque.front() == 0
    assert deque.back() == 3
    assert deque.full() == True
    assert deque.empty() == False
    
    assert deque.pop_front() == 0
    assert deque.pop_back() == 3
    assert deque.size() == 2
    
    deque.push_back(4)
    deque.push_back(5)
    assert deque.size() == 4
    
    deque.resize(6)
    assert deque.size() == 4
    assert deque.full() == False
    assert deque.front() == 1
    assert deque.back() == 5
    
    deque.push_back(6)
    deque.push_back(7)
    assert deque.full() == True

    deque.push_back(3)
    assert deque.front() == 2
    assert deque.back() == 3
    
    deque.push_front(-3)
    deque.push_front(-1)
    assert deque.front() == -1
    assert deque.back() == 6


def test_edge_cases_empty_deque():
    deque = CircularDeque(2, push_force=False)
    
    assert deque.empty() == True
    assert deque.full() == False
    assert deque.size() == 0
    
    with pytest.raises(IndexError):
        deque.pop_front()
    
    with pytest.raises(IndexError):
        deque.pop_back()
    
    with pytest.raises(IndexError):
        deque.front()
    
    with pytest.raises(IndexError):
        deque.back()


def test_edge_cases_full_deque():
    deque = CircularDeque(2, push_force=False)
    
    deque.push_back(1)
    deque.push_back(2)
    
    assert deque.full() == True
    
    with pytest.raises(IndexError):
        deque.push_back(3)
    
    with pytest.raises(IndexError):
        deque.push_front(0)


def test_edge_cases_single_element():
    deque = CircularDeque(1, push_force=False)
    
    deque.push_front(42)
    
    assert deque.size() == 1
    assert deque.full() == True
    assert deque.empty() == False
    assert deque.front() == 42
    assert deque.back() == 42
    
    assert deque.pop_front() == 42
    assert deque.empty() == True


def test_edge_cases_negative_capacity():
    with pytest.raises(ValueError):
        deque = CircularDeque(-1, True)

    deque = CircularDeque(4, True)
    deque.push_back(1)

    with pytest.raises(ValueError):
        deque.resize(-1)


def test_resize_to_shorter_functionality():
    deque = CircularDeque(4, push_force=True)
    for i in range(4):
        deque.push_back(i)
    
    deque.resize(2)
    assert deque.size() == 2
    assert deque.front() == 0
    assert deque.back() == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
