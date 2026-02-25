import React, { useId } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import LabeledInput from "./LabeledInput";
import CheckboxField from "./CheckboxField";
import TextLink from "./TextLink";
import PrimaryButton from "./PrimaryButton";

export default function SignInCard({
  usernameOrEmail,
  password,
  rememberMe,
  onUsernameOrEmailChange = () => {},
  onPasswordChange = () => {},
  onRememberMeChange = () => {},
  onForgotPassword = () => {},
  forgotPasswordHref = "#",
  onSubmit = () => {},
  loading = false,
  headerIcon: HeaderIcon = User,
}) {
  const intl = useIntl();

  const uid = useId();
  const usernameId = `${uid}-username`;
  const passwordId = `${uid}-password`;
  const rememberId = `${uid}-remember`;

  return (
    <section
      aria-label={intl.formatMessage({ id: "signInCard.ariaLabel" })}
      className="w-full rounded-[14px] border border-[#E5E7EB] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="px-6 pt-6">
        <div className="flex items-center gap-1.5">
          <HeaderIcon className="h-5 w-5 text-[#0A0A0A]" aria-hidden="true" />
          <h2 className="text-[16px] leading-4 font-medium tracking-[-0.3125px] text-[#0A0A0A]">
            {intl.formatMessage({ id: "signInCard.title" })}
          </h2>
        </div>

        <p className="mt-2 text-[16px] leading-6 font-normal tracking-[-0.3125px] text-[#717182]">
          {intl.formatMessage({ id: "signInCard.description" })}
        </p>
      </div>

      <form
        className="px-6 pt-4 pb-6"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({
            usernameOrEmail,
            password,
            rememberMe,
          });
        }}
      >
        <div className="flex flex-col gap-4">
          <LabeledInput
            id={usernameId}
            label={intl.formatMessage({ id: "signInCard.usernameOrEmailLabel" })}
            type="text"
            value={usernameOrEmail}
            placeholder={intl.formatMessage({ id: "signInCard.usernameOrEmailPlaceholder" })}
            onChange={onUsernameOrEmailChange}
            autoComplete="username"
            inputMode="email"
          />

          <LabeledInput
            id={passwordId}
            label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
            type="password"
            value={password}
            placeholder={intl.formatMessage({ id: "signInCard.passwordPlaceholder" })}
            onChange={onPasswordChange}
            autoComplete="current-password"
          />

          <div className="flex items-center justify-between">
            <CheckboxField
              id={rememberId}
              checked={rememberMe}
              label={intl.formatMessage({ id: "signInCard.rememberMe" })}
              onChange={onRememberMeChange}
            />

            <TextLink
              href={forgotPasswordHref}
              onClick={(e) => {
                onForgotPassword(e);
              }}
            >
              {intl.formatMessage({ id: "signInCard.forgotPassword" })}
            </TextLink>
          </div>

          <PrimaryButton disabled={loading}>
            {loading
              ? intl.formatMessage({ id: "signInCard.continuing" })
              : intl.formatMessage({ id: "signInCard.continue" })}
          </PrimaryButton>
        </div>
      </form>
    </section>
  );
}