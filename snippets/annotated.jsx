// A screenshot with numbered markers. The numbers match the page's anatomy table.
// Marker positions are percentages of the image, measured on the live app when
// the screenshot was taken, so they stay on the element as the image scales.
// size="sm" draws smaller dots, for a dense screenshot shown at a small scale.
export const Annotated = ({ src, alt, caption, markers = [], size }) => (
  <figure className={"ann not-prose" + (size === "sm" ? " ann-sm" : "")}>
    <div className="ann-frame">
      <img src={src} alt={alt} className="ann-img" />
      {markers.map((m) => (
        <span key={m.n} className="ann-dot" style={{ left: m.x + "%", top: m.y + "%" }} aria-hidden="true">
          {m.n}
        </span>
      ))}
    </div>
    {caption ? <figcaption className="ann-cap">{caption}</figcaption> : null}
  </figure>
);
