import React from "react";
import { useIntl } from "react-intl";
import { Check } from "lucide-react";

function noop() {}

export default function RememberMeRow({
  rememberMe,
  onRememberMeChange = noop,
  onForgotPassword = noop,
}) {
  const intl = useIntl();

  return (
    <div className="flex w-full items-center justify-between gap-4">
      <label className="flex cursor-pointer items-center gap-2">
        <span className="relative grid h-[13px] w-[13px] place-items-center rounded-[3px] border border-[#cbd5e1] bg-white">
          <input
            type="checkbox"
            checked={rememberMe}
            onChange={(e) => onRememberMeChange(e.target.checked)}
            className="absolute inset-0 cursor-pointer opacity-0"
            aria-label="Remember me"
          />
          {rememberMe ? (
            <Check className="h-3 w-3 text-[#155dfc]" aria-hidden="true" />
          ) : null}
        </span>

        <span className="text-base font-medium leading-6 tracking-[-0.3125px] text-[#4a5565]">
          {intl.formatMessage({ id: "rememberMeRow.rememberMe" })}
        </span>
      </label>

      <button
        type="button"
        onClick={onForgotPassword}
        className="text-sm leading-5 tracking-[-0.1504px] text-[#155dfc] hover:underline"
      >
        {intl.formatMessage({ id: "rememberMeRow.forgotPassword" })}
      </button>
    </div>
  );
}