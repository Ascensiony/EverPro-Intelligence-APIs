import * as React from "react";

function SvgComponent(props) {
  return (
    <svg viewBox="0 0 59.23 30.21" {...props}>
      <defs>
        <linearGradient
          id="vivo-gradient"
          x1={-8.33}
          y1={22.34}
          x2={-8.37}
          y2={14.64}
          gradientTransform="translate(37.96 -15.66)"
          gradientUnits="userSpaceOnUse"
        >
          <stop offset={0} stopColor="#fff" />
          <stop offset={0.28} stopColor={props.color === "#b0b0b0" ? "#c8c8c8" : "#222"} stopOpacity={0.76} />
          <stop offset={0.93} stopColor="#424242" stopOpacity={0.16} />
          <stop offset={1} stopColor="#333" stopOpacity={0.1} />
        </linearGradient>
        <style>{".prefix__cls-3{fill:#b0b0b0}"}</style>
      </defs>
      <g id="prefix__Layer_2" data-name="Layer 2">
        <g id="prefix__Layer_1-2" data-name="Layer 1">
          <g id="prefix__vivo">
            <g id="prefix__box">
              <path
                transform="rotate(180 29.615 17.445)"
                fill={props.color === "#b0b0b0" ? "#434343" : "#222"}
                d="M0 4.68h59.23v25.53H0z"
              />
              <path
                fill="url(#vivo-gradient)"
                d="M59.23 4.68H0L10 0h39.23l10 4.68z"
              />
            </g>
            <g id="prefix__vivo-2" data-name="vivo">
              <path
                fill={props.color}
                d="M42.48 24.48a4.38 4.38 0 01-4.35-3.54 4.21 4.21 0 012.19-4.46A4.5 4.5 0 0146.23 18a4.19 4.19 0 01-1.38 5.87 4.53 4.53 0 01-2.37.61zm-1.8-4.29A1.75 1.75 0 0042.47 22a1.74 1.74 0 100-3.48 1.75 1.75 0 00-1.79 1.67zM32.68 20.6l.86-1.69 1.35-2.66a.79.79 0 011.19-.39l.94.51a.88.88 0 01.37 1.34c-.4.72-.82 1.44-1.24 2.16-.64 1.11-1.28 2.22-1.93 3.33-.08.14-.18.27-.28.41a1.74 1.74 0 01-2.88-.16c-.49-.94-1-1.85-1.54-2.77L28 17.9a3.28 3.28 0 01-.24-.54.65.65 0 01.24-.76 11.82 11.82 0 011.2-.79.62.62 0 011 .28c.53.9 1 1.81 1.55 2.72l.88 1.61zM17.31 20.65l.15-.28 2-4a.81.81 0 011.3-.4l.9.49a.88.88 0 01.36 1.28l-3.15 5.45a4 4 0 01-.38.54 1.72 1.72 0 01-2.41.26 2.58 2.58 0 01-.54-.69c-1-1.81-2-3.61-3-5.43-.41-.74-.33-1 .38-1.48l.65-.43a.74.74 0 011.21.28c.77 1.36 1.52 2.72 2.28 4.08.1.08.16.19.25.33zM26.44 20.16v3.4a1.58 1.58 0 01-.05.38.54.54 0 01-.57.45H24.2c-.45 0-.67-.25-.67-.74v-6.7a2.71 2.71 0 010-.29c.05-.38.21-.58.59-.59a17 17 0 011.75 0c.42 0 .55.2.56.64v3.48zM26.65 13.11A1.63 1.63 0 1125 11.48a1.63 1.63 0 011.65 1.63z"
              />
            </g>
          </g>
        </g>
      </g>
    </svg>
  );
}

export default SvgComponent;

