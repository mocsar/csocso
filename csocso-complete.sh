_csocso_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _CSOCSO_COMPLETE=complete $1 ) )
    return 0
}

complete -F _csocso_completion -o default csocso;
