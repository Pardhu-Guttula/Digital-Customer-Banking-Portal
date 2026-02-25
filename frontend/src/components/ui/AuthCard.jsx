import React from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";

export default function AuthCard({
  title,
  description,
  children,
  onForgotPassword = () => {},
  forgotPasswordLabel,
  forgotPasswordHref,
}) {
  const intl = useIntl();

  const resolvedForgotPasswordLabel =
    forgotPasswordLabel ?? intl.formatMessage({ id: "common.forgotPassword" });

  return (
    <section
      aria-label="Sign in"
      className="w-full rounded-[14px] border border-[#e5e7eb] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="flex flex-col gap-1.5 px-6 pt-6">
        <div className="flex items-center gap-1.5">
          <User className="h-5 w-5 text-[#0a0a0a]" aria-hidden="true" />
          <h2 className="text-[16px] font-medium leading-4 tracking-[-0.3125px] text-[#0a0a0a]">
            {title ?? intl.formatMessage({ id: "authCard.title" })}
          </h2>
        </div>
        <p className="text-[16px] font-normal leading-6 tracking-[-0.3125px] text-[#717182]">
          {description ?? intl.formatMessage({ id: "authCard.description" })}
        </p>
      </div>

      <div className="px-6 pb-6 pt-4">{children}</div>

      <div className="sr-only">
        <a
          href={forgotPasswordHref || "#"}
          onClick={(e) => {
            if (!forgotPasswordHref) e.preventDefault();
            onForgotPassword();
          }}
        >
          {resolvedForgotPasswordLabel}
        </a>
      </div>
    </section>
  );
}