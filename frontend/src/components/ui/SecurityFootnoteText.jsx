import React from "react";

export default function SecurityFootnoteText({ text }) {
  return (
    <p
      className="text-center text-[14px] leading-[20px] tracking-[-0.1504px] text-[#4a5565]"
      aria-label={text}
    >
      {text}
    </p>
  );
}