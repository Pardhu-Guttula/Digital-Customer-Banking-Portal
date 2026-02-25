import React from "react";
import { useIntl } from "react-intl";
import { Check } from "lucide-react";
import cn from "../utils/cx";

function noop() {}

export default function RememberMeRow({
  checked,
  onCheckedChange = noop,
  onForgotPassword = noop,
  forgotHref,
}) {
  const intl = useIntl();

  return (
    <div className="flex w-full items-center justify-between">
      <label className="flex cursor-pointer items-center gap-2 select-none">
        <span className="relative inline-flex h-[13px] w-[13px] items-center justify-center">
          <input
            type="checkbox"
            checked={checked}
            onChange={(e) => onCheckedChange(e.target.checked)}
            className={cn(
              "peer h-[13px] w-[13px] appearance-none rounded-[3px] border border-[#cfd3dc] bg-white outline-none",
              "focus:ring-2 focus:ring-[#155dfc]/20"
            )}
            aria-label="Remember me"
          />
          <Check
            className="pointer-events-none absolute h-3 w-3 text-[#155dfc] opacity-0 peer-checked:opacity-100"
            aria-hidden="true"
          />
        </span>

        <span className="text-[16px] font-medium leading-6 tracking-[-0.3125px] text-[#4a5565]">
          {intl.formatMessage({ id: "rememberMeRow.rememberMe" })}
        </span>
      </label>

      {forgotHref ? (
        <a
          href={forgotHref}
          onClick={(e) => {
            onForgotPassword();
          }}
          className="text-[14px] font-normal leading-5 tracking-[-0.1504px] text-[#155dfc] hover:underline"
        >
          {intl.formatMessage({ id: "rememberMeRow.forgotPassword" })}
        </a>
      ) : (
        <button
          type="button"
          onClick={onForgotPassword}
          className="text-[14px] font-normal leading-5 tracking-[-0.1504px] text-[#155dfc] hover:underline"
        >
          {intl.formatMessage({ id: "rememberMeRow.forgotPassword" })}
        </button>
      )}
    </div>
  );
}