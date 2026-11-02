export function ProductDiagram() {
  return (
    <svg viewBox="0 0 700 200" role="img" aria-label="ম্যাট্রিক্স গুণে A-এর একটি সারি ও B-এর একটি কলাম দিয়ে entry বের করা">
      <text x="350" y="22" textAnchor="middle" className="svg-label">প্রতি entry = একটি সারির সঙ্গে একটি কলামের dot product</text>
      <rect x="30" y="42" width="225" height="112" rx="12" className="svg-blue" />
      <text x="142" y="68" textAnchor="middle" className="svg-caption">A-এর ১ম সারি</text>
      <rect x="66" y="82" width="166" height="34" rx="6" className="svg-highlight" />
      <text x="93" y="104" textAnchor="middle" className="svg-math">1</text><text x="152" y="104" textAnchor="middle" className="svg-math">2</text><text x="211" y="104" textAnchor="middle" className="svg-math">0</text>
      <text x="282" y="104" textAnchor="middle" className="svg-math">·</text>
      <rect x="310" y="42" width="142" height="132" rx="12" className="svg-mint" />
      <text x="381" y="65" textAnchor="middle" className="svg-caption">B-এর ১ম কলাম</text>
      <rect x="328" y="76" width="36" height="78" rx="6" className="svg-highlight" />
      <text x="346" y="94" textAnchor="middle" className="svg-math">3</text><text x="381" y="94" textAnchor="middle" className="svg-math">1</text><text x="416" y="94" textAnchor="middle" className="svg-math">2</text>
      <text x="346" y="120" textAnchor="middle" className="svg-math">4</text><text x="381" y="120" textAnchor="middle" className="svg-math">5</text><text x="416" y="120" textAnchor="middle" className="svg-math">6</text>
      <text x="346" y="146" textAnchor="middle" className="svg-math">2</text><text x="381" y="146" textAnchor="middle" className="svg-math">3</text><text x="416" y="146" textAnchor="middle" className="svg-math">1</text>
      <path d="M470 104h48m-10-10 10 10-10 10" className="svg-arrow" />
      <rect x="537" y="42" width="140" height="112" rx="12" className="svg-gold" />
      <text x="607" y="73" textAnchor="middle" className="svg-caption">ফল (1,1)</text>
      <text x="607" y="111" textAnchor="middle" className="svg-math">1·3+2·4+0·2=11</text>
    </svg>
  );
}

export function TransformDiagram() {
  const grid = Array.from({ length: 5 }, (_, k) => k);
  return (
    <svg viewBox="0 0 700 220" role="img" aria-label="T(x,y)=(x+y,y) shear-এ unit grid এবং basis vector-এর রূপান্তর">
      <defs><marker id="transformArrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="#168575" /></marker></defs>
      <text x="160" y="22" textAnchor="middle" className="svg-label">আগে: standard grid</text>
      <text x="500" y="22" textAnchor="middle" className="svg-label">পরে: T(x,y)=(x+y,y)</text>
      <g stroke="#cbd7e3" strokeWidth="1">
        {[70,100,130,160,190,220,250].map((x) => <path key={`lv${x}`} d={`M${x} 70V190`} />)}
        {[70,100,130,160,190].map((y) => <path key={`lh${y}`} d={`M70 ${y}H250`} />)}
      </g>
      <g stroke="#b8c7d6" strokeWidth="1">
        {grid.map((k) => <path key={`rh${k}`} d={`M${385 + 30*k} ${190 - 30*k}H${505 + 30*k}`} />)}
        {grid.map((k) => <path key={`rv${k}`} d={`M${385 + 30*k} 190L${505 + 30*k} 70`} />)}
      </g>
      <path d="M70 190H100M70 190V160" stroke="#2467b2" strokeWidth="3" />
      <path d="M385 190H415M385 190L415 160" stroke="#168575" strokeWidth="4" markerEnd="url(#transformArrow)" />
      <text x="164" y="187" className="svg-caption">e₁</text><text x="74" y="96" className="svg-caption">e₂</text>
      <text x="418" y="188" className="svg-caption">T(e₁)=e₁</text><text x="419" y="157" className="svg-caption">T(e₂)=(1,1)</text>
      <text x="500" y="210" textAnchor="middle" className="svg-caption">grid বেঁকে যায়, কিন্তু linearity বজায় থাকে</text>
    </svg>
  );
}

export function EigenDiagram() {
  return (
    <svg viewBox="0 0 600 205" role="img" aria-label="A=diag(2,1)-এ e1-এর দিক একই থাকে ও দ্বিগুণ হয়; সাধারণ vector-এর দিক বদলায়">
      <defs>
        <marker id="eigenBlue" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="#2467b2" /></marker>
        <marker id="eigenGreen" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="#168575" /></marker>
        <marker id="eigenGold" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="#d68a23" /></marker>
      </defs>
      <path d="M45 160H270M60 180V42M325 160H580M340 180V42" className="svg-axis" />
      <text x="157" y="23" textAnchor="middle" className="svg-label">আগে: v=e₁=(1,0)</text>
      <text x="452" y="23" textAnchor="middle" className="svg-label">পরে: Av=2e₁=(2,0)</text>
      <path d="M60 160H120" stroke="#2467b2" strokeWidth="4" markerEnd="url(#eigenBlue)" />
      <path d="M340 160H460" stroke="#168575" strokeWidth="4" markerEnd="url(#eigenGreen)" />
      <path d="M60 160L120 100" stroke="#d68a23" strokeWidth="3" strokeDasharray="5 4" markerEnd="url(#eigenGold)" />
      <path d="M340 160L460 100" stroke="#d68a23" strokeWidth="3" strokeDasharray="5 4" markerEnd="url(#eigenGold)" />
      <text x="78" y="149" className="svg-caption">e₁</text><text x="390" y="149" className="svg-caption">2e₁</text>
      <text x="126" y="96" className="svg-caption">সাধারণ v=(1,1)</text><text x="463" y="96" className="svg-caption">Av=(2,1)</text>
      <text x="300" y="198" textAnchor="middle" className="svg-caption">e₁ একই রেখায় থাকে → eigenvector; (1,1)-এর দিক বদলায় → সাধারণ vector</text>
    </svg>
  );
}
