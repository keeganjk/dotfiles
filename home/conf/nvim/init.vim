set number
set clipboard+=unnamedplus
set autoindent smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set mouse=n

nnoremap <esc> :noh<return><esc>

call plug#begin()

Plug 'guns/xterm-color-table.vim'
Plug 'keeganjk/onedark.vim'
Plug 'skammer/vim-css-color'
Plug 'xuhdev/vim-latex-live-preview', { 'for': 'tex' }
Plug 'Raimondi/delimitMate'
Plug 'mattn/emmet-vim'

call plug#end()

:function WriteEnglish()
    :set spell spelllang=en_US
    :set linebreak
:endfunction

:function CompileLaTeX()
    :!pdflatex %
:endfunction

:function CompileBibLaTeX()
    :!pdflatex % && biber %:r && pdflatex %
:endfunction

nnoremap <C-e> :call WriteEnglish()<CR>
nnoremap <C-l> :call CompileBibLaTeX()<CR>
nnoremap <C-L> :call CompileBibLaTeX()<CR>
nnoremap S :%s//g<Left><Left>

let g:user_emmet_mode='n'
let g:user_emmet_leader_key=','

let g:onedark_hide_endofbuffer=1
let g:onedark_termcolors=256
let g:onedark_terminal_italics=1
let g:airline_theme='onedark'
let g:tex_indent_items=0
let g:tex_indent_and=0
let g:tex_indent_brace=0
colorscheme onedark
hi Normal guibg=NONE ctermbg=NONE
