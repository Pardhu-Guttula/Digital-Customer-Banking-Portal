import React from "react";
import { useIntl } from "react-intl";

export default function SecurityCaption({ text }) {
  const intl = useIntl();

  return (
    <footer className="text-center">
      <p className="text-[14px] leading-5 text-[#4a5565] tracking-[-0.1504px]">
        {text ?? intl.formatMessage({ id: "securityCaption.text" })}
      </p>
    </footer>
  );
}