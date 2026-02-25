import React from "react";
import { useIntl } from "react-intl";

export default function TextLink({ label, onClick = () => {} }) {
  useIntl();

  return (
    <button
      type="button"
      onClick={onClick}
      className="text-[14px] leading-5 tracking-[-0.1504px] text-[#155DFC] hover:underline focus:outline-none focus:ring-2 focus:ring-[#155DFC]/20 rounded"
    >
      {label}
    </button>
  );
}