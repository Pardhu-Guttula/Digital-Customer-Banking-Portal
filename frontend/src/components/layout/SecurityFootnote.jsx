import React from "react";
import { useIntl } from "react-intl";

export default function SecurityFootnote({ text }) {
  const intl = useIntl();
  const resolvedText =
    text ?? intl.formatMessage({ id: "securityFootnote.text" });

  return (
    <footer className="flex items-center justify-center">
      <p className="text-center text-[14px] leading-5 tracking-[-0.1504px] text-[#4a5565]">
        {resolvedText}
      </p>
    </footer>
  );
}