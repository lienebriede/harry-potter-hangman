def nagini(tries):
    """
    This list takes too much space
    so it is linked to the main file,
    each try is one list element from score list
    """
    score = [
    r"""
             \     /    !     
            (O)---(O)     !
             \_____/    
                '-----<   
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\  
    """,
    
    r"""
            ^     ^     ?
           (O)---(O)  ?   
            \_____/   
              \vv\
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\    
    """,
    
    r"""
            _     _  z
           (-)---(O)    z
            \_____/    z
              \vv\
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\
    """,

    r"""
            _     _   z   
           (-)---(-)     z
            \_____/    z
              \vv\
               |vv|     /\
                \vv\____\v\
                 \v_v_v_v_v\
    """     
    ]    
    return score[tries]


 
       