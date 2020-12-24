import * as React from "react";

function Apple(props) {
   return (
      <svg viewBox="0 0 59.23 30.21" {...props}>
         <defs>
            <linearGradient
               id="apple__linear-gradient"
               x1={-8.33}
               y1={22.34}
               x2={-8.37}
               y2={14.64}
               gradientTransform="translate(37.96 -15.66)"
               gradientUnits="userSpaceOnUse"
            >
               <stop offset={0} stopColor="#fff"/>
               <stop offset={0.28} stopColor={props.color === "#b0b0b0" ? "#c8c8c8" : "#222"} stopOpacity={0.76}/>
               <stop offset={0.93} stopColor="#424242" stopOpacity={0.16}/>
               <stop offset={1} stopColor="#333" stopOpacity={0.1}/>
            </linearGradient>
         </defs>
         <g id="__Layer_2" data-name="Layer 2">
            <g id="__Layer_1-2" data-name="Layer 1">
               <g id="__apple">
                  <g id="prefix__box">
                     <path
                        transform="rotate(180 29.615 17.445)"
                        fill={props.color === "#b0b0b0" ? "#434343" : "#222"}
                        d="M0 4.68h59.23v25.53H0z"
                     />
                     <path
                        fill="url(#apple__linear-gradient)"
                        d="M59.23 4.68H0L10 0h39.23l10 4.68z"
                     />
                  </g>
                  <g id="prefix__apple-2" data-name="apple">
                     <path
                        fill={props.color}
                        d="M36.75 13.68c-.25.24-.5.46-.74.7a4 4 0 00-1.16 2.13 4.17 4.17 0 000 1.41 4.22 4.22 0 001.69 2.8c.23.16.49.27.76.42-.12.31-.24.64-.38 1a11.51 11.51 0 01-1.57 2.55 4.28 4.28 0 01-1.24 1.08 2.1 2.1 0 01-1.61.19c-.44-.12-.87-.26-1.3-.4a3.64 3.64 0 00-1.7-.19 4.83 4.83 0 00-1.18.34 4.41 4.41 0 01-1.19.35 2.3 2.3 0 01-1.65-.51 6 6 0 01-1.4-1.55 13.69 13.69 0 01-1.51-3 10.26 10.26 0 01-.57-2.49 8.26 8.26 0 01.25-3.05 5.18 5.18 0 011.61-2.6A3.61 3.61 0 0126 12a6.54 6.54 0 012 .24l1.57.38a1.68 1.68 0 00.86-.07c.45-.12.89-.27 1.34-.4a5.44 5.44 0 011.45-.25 4.09 4.09 0 013.22 1.45z"
                     />
                     <path
                        fill={props.color}
                        d="M33.1 7.74a4.9 4.9 0 010 .54 4.09 4.09 0 01-.5 1.81 4.43 4.43 0 01-1.39 1.59 2.52 2.52 0 01-1.23.45l-.56.07v-.49A5.19 5.19 0 0130 9.87a3.7 3.7 0 011.7-1.66 7.63 7.63 0 011.3-.46z"
                     />
                  </g>
               </g>
            </g>
         </g>
      </svg>
   );
}

export default Apple;

