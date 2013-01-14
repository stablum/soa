% IMPORT_FROM_STATS
% drag & drop stats. import as column vectors
%---------------------------------
% countsteps 
% expnum 
% meanedgesimportance
% stdedgesimportance
% numkills
% pathlength
% totalweight
%----------------------------------

% from columns to matrix using steps and expnum: rows=RUNS, columns=exp
% for each variable, take mean and 25/75%iles of each cycle
% make graphs var vs cycle
% make anova of [final] values
%----------------------------------
%% from columns to matrix using steps and expnum: rows=RUNS, columns=exp
expnum=expnum+1; % DO Once, better to FIX BEFORE
%%
max_num_steps=max(countsteps);
max_num_exps=max(expnum);
steps=[1:max_num_steps];
exps=[1:max_num_exps];
ss=0;
all_p_l=[];all_std_imp=[];all_mean_imp=[];all_n_kill=[];all_tot_w=[];
for col= exps
    for row=steps
        ss=ss+1;
%         if mod(ss,max_num_steps+1)==0
%             ss=ss+1;
%         end
    if row==max_num_steps && col==max_num_exps
    else
            all_p_l(row,col)=pathlength(ss);
            all_std_imp(row,col)=stdedgesimportance(ss);
            all_mean_imp(row,col)=meanedgesimportance(ss);
            all_n_kill(row,col)=numkills(ss);
            all_tot_w(row,col)=totalweight(ss);
    end
    end
end
% p_l,std_imp,mean_imp,n_kill,tot_w
steps=1:max_num_steps-1;
all_p_l=all_p_l(steps,:); all_std_imp=all_std_imp(steps,:); all_mean_imp=all_mean_imp(steps,:); all_n_kill=all_n_kill(steps,:); all_tot_w=all_tot_w(steps,:);
%% for each variable, take mean and 25/75%iles of each cycle

p_l.p25=prctile(all_p_l',25);    std_imp.p25=prctile(all_std_imp',25);    mean_imp.p25=prctile(all_mean_imp',25);  n_kill.p25=prctile(all_n_kill',25);  tot_w.p25=prctile(all_tot_w',25);       
p_l.p75=prctile(all_p_l',75);    std_imp.p75=prctile(all_std_imp',75);    mean_imp.p75=prctile(all_mean_imp',75);  n_kill.p75=prctile(all_n_kill',75);   tot_w.p75=prctile(all_tot_w',75);     
p_l.avg=mean(all_p_l');          std_imp.avg=mean(all_std_imp');             mean_imp.avg=mean(all_mean_imp');         n_kill.avg=mean(all_n_kill');          tot_w.avg=mean(all_tot_w');          

%% make graphs variable (mean,25 and 75 percentile) x cycle
figure;
p1=plot(steps,p_l.avg,'--'); hold on; p2=plot(steps,p_l.p25,'--'); hold on; p3=plot(steps,p_l.p75,'--'); hold on;  
title('path length over cycles')
ylabel('path length'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure;
p1=plot(steps,std_imp.avg); hold on; p2=plot(steps,std_imp.p25,'--'); hold on; p3=plot(steps,std_imp.p75,'--'); hold on;  
title('stand deviation of the importance of the edges over the cycles');
ylabel('std dev of edge importance'); xlabel('cycles'); legend([p1,p2,p3],'mean','pile25','pile75')

figure;
p1=plot(steps,mean_imp.avg); hold on; p2=plot(steps,mean_imp.p25,'--'); hold on; p3=plot(steps,mean_imp.p75,'--'); hold on;  
title('mean edge importance over cycles')
ylabel('mean edge importance'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure;
p1=plot(steps,n_kill.avg); hold on; p2=plot(steps,n_kill.p25,'--'); hold on; p3=plot(steps,n_kill.p75,'--'); hold on;  
title('number of dead edges over cycles')
ylabel('number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure;
p1=plot(steps,tot_w.avg); hold on; p2=plot(steps,tot_w.p25,'--'); hold on; p3=plot(steps,tot_w.p75,'--'); hold on;
title('total weight of the graph over cycles')
ylabel('total weight of the graph'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75');

%% make cumulative of killed edges x cycle

figure;
p1=plot(steps,cumsum(n_kill.avg)); hold on; p2=plot(steps,(n_kill.p25),'--'); hold on; p3=plot(steps,cumsum(n_kill.p75),'--'); hold on;  
title('number of dead edges over cycles')
ylabel('number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

%% make anova of [final] values
countsteps

expnum

meanedgesimportance

stdedgesimportance

numkills

pathlength

totalweight