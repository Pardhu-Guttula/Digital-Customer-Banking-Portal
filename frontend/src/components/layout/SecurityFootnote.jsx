import React from "react";
import { useIntl } from "react-intl";

export default function SecurityFootnote({ text }) {
  const intl = useIntl();

  return (
    <footer className="text-center">
      <p className="text-[14px] leading-5 tracking-[-0.1504px] text-[#4A5565]">
        {text ??
          intl.formatMessage({
            id: "securityFootnote.text",
          })}
      </p>
    </footer>
  );
}