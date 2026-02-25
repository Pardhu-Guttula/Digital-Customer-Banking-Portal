import React from "react";
import { useIntl } from "react-intl";

export default function SecurityNote({ text }) {
  const intl = useIntl();

  const resolvedText =
    text ?? intl.formatMessage({ id: "securityNote.text" });

  return (
    <footer className="text-center">
      <p className="text-[14px] leading-5 tracking-[-0.1504px] text-[#4a5565]">
        {resolvedText}
      </p>
    </footer>
  );
}