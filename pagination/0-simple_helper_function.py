#!/usr/bin/env python3
"""task 0 0-simple_helper_function"""

def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple of start and end index for pagination.
    
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    
    Returns:
        tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
