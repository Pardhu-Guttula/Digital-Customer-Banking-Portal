import React from "react";
import { useIntl } from "react-intl";

export default function SecurityNote({ text }) {
  const intl = useIntl();

  return (
    <footer className="flex items-center justify-center">
      <p className="text-center text-[14px] font-normal leading-5 tracking-[-0.1504px] text-[#4a5565]">
        {text ?? intl.formatMessage({ id: "securityNote.text" })}
      </p>
    </footer>
  );
}