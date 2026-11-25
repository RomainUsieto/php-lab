export const escapeHtml = text => String(text??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function highlight(text) {
  const re=/(\/\*[\s\S]*?\*\/|\/\/[^\n]*|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\$[a-zA-Z_][\w]*|\b(?:function|return|class|public|private|protected|static|new|extends|if|else|elseif|foreach|as|for|while|switch|case|break|default|echo|include|true|false|null|parent|self)\b|\b\d+(?:\.\d+)?\b)/g;
  let out='',pos=0;for(const m of text.matchAll(re)){out+=escapeHtml(text.slice(pos,m.index));let cls=m[0].startsWith('//')||m[0].startsWith('/*')?'comment':/^["']/.test(m[0])?'string':m[0][0]==='$'?'variable':/^\d/.test(m[0])?'number':'keyword';out+=`<span class="tok-${cls}">${escapeHtml(m[0])}</span>`;pos=m.index+m[0].length;}return out+escapeHtml(text.slice(pos));
}
export function mountEditor(root,value,onChange,disabled=false) {
  root.innerHTML=`<div class="editor-title"><span>réponse.php</span><span>PHP · saisie libre</span></div><div class="editor-body"><div class="line-numbers" aria-hidden="true"></div><div class="editor-surface"><pre aria-hidden="true"><code></code></pre><textarea aria-label="Votre code PHP" spellcheck="false" maxlength="30000" autocapitalize="off" autocomplete="off" autocorrect="off" ${disabled?'readonly':''}></textarea></div></div>`;
  const input=root.querySelector('textarea'),pre=root.querySelector('pre'),numbers=root.querySelector('.line-numbers');input.value=value||'';
  function paint(){pre.querySelector('code').innerHTML=highlight(input.value)+'\n';numbers.textContent=Array.from({length:input.value.split('\n').length},(_,i)=>i+1).join('\n');pre.scrollTop=input.scrollTop;pre.scrollLeft=input.scrollLeft;numbers.scrollTop=input.scrollTop;}
  input.addEventListener('input',()=>{paint();onChange(input.value);});input.addEventListener('scroll',paint);
  input.addEventListener('keydown',e=>{if(disabled)return;if(e.key==='Tab'){e.preventDefault();const a=input.selectionStart,b=input.selectionEnd;input.setRangeText('    ',a,b,'end');paint();onChange(input.value);}if(e.key==='Enter'){e.preventDefault();const p=input.selectionStart;const line=input.value.slice(0,p).split('\n').pop();const indent=(line.match(/^\s*/)?.[0]||'')+(line.trimEnd().endsWith('{')?'    ':'');input.setRangeText('\n'+indent,p,input.selectionEnd,'end');paint();onChange(input.value);}});
  paint();return input;
}
