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
Plug 'ap/vim-css-color'
Plug 'xuhdev/vim-latex-live-preview', { 'for': 'tex' }
Plug 'Raimondi/delimitMate'
Plug 'mattn/emmet-vim'

call plug#end()

:function WriteEnglish()
    :set spell spelllang=en_US
    :set linebreak
:endfunction

:function CompileLaTeX()
    :w
    :!pdflatex % && [[ -z $(ls | grep .bib) ]] || biber %:r && pdflatex %
:endfunction

nnoremap <C-e> :call WriteEnglish()<CR>
nnoremap <C-l> :call CompileLaTeX()<CR>
nnoremap <C-p> :PlugInstall<CR>
nnoremap <C-s> :%s//g<Left><Left>
nnoremap <C-v> :so $MYVIMRC<CR>

let g:user_emmet_mode='n'
let g:user_emmet_leader_key=','
let g:onedark_hide_endofbuffer=1
let g:onedark_termcolors=256
let g:onedark_terminal_italics=1
let g:airline_theme='onedark'
let g:tex_indent_items=0
let g:tex_indent_and=0
let g:tex_indent_brace=0
colo onedark
hi Normal guibg=NONE ctermbg=NONE
