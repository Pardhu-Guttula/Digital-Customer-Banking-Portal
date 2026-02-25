import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({ children, disabled, onClick = () => {} }) {
  const intl = useIntl();

  return (
    <button
      type="submit"
      disabled={disabled}
      onClick={(e) => onClick(e)}
      className="h-11 w-full rounded-lg bg-[#030213] text-white text-[14px] leading-5 font-medium tracking-[-0.1504px] hover:bg-[#0A0A1A] active:bg-[#00010A] disabled:opacity-60 disabled:cursor-not-allowed focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/35 focus-visible:ring-offset-2 focus-visible:ring-offset-white"
    >
      {children ?? intl.formatMessage({ id: "primaryButton.label" })}
    </button>
  );
}